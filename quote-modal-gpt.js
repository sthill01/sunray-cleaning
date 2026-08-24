(function () {
  var ctaEventNames = {
    quote: "sunray_quote_cta_click",
    call: "sunray_call_cta_click",
    text: "sunray_text_cta_click",
    submit: "sunray_quote_submit_click",
  };
  var attributionStorageKey = "sunray_attribution_v1";
  var clickIdFieldNames = ["gclid", "gbraid", "wbraid", "msclkid", "fbclid", "ttclid", "li_fat_id"];
  var utmFieldNames = ["utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content", "utm_id"];
  var attributionFieldNames = clickIdFieldNames.concat(utmFieldNames, [
    "first_landing_page",
    "landing_page",
    "referrer",
    "attribution_updated_at",
  ]);
  var modal;
  var lastFocused;
  var currentAttribution = {};

  function getFocusable(container) {
    return Array.prototype.slice.call(
      container.querySelectorAll('a[href], button:not([disabled]), input:not([disabled]), select:not([disabled]), textarea:not([disabled]), [tabindex]:not([tabindex="-1"])')
    );
  }

  function openModal(event) {
    if (!modal) return;
    if (event) event.preventDefault();
    lastFocused = document.activeElement;
    modal.classList.add("is-open");
    modal.setAttribute("aria-hidden", "false");
    document.body.classList.add("modal-open");
    var firstField = modal.querySelector("input, select, textarea, button");
    if (firstField) firstField.focus();
  }

  function closeModal() {
    if (!modal) return;
    modal.classList.remove("is-open");
    modal.setAttribute("aria-hidden", "true");
    document.body.classList.remove("modal-open");
    if (lastFocused && typeof lastFocused.focus === "function") lastFocused.focus();
  }

  function trapFocus(event) {
    if (!modal || !modal.classList.contains("is-open") || event.key !== "Tab") return;
    var focusable = getFocusable(modal);
    if (!focusable.length) return;
    var first = focusable[0];
    var last = focusable[focusable.length - 1];
    if (event.shiftKey && document.activeElement === first) {
      event.preventDefault();
      last.focus();
    } else if (!event.shiftKey && document.activeElement === last) {
      event.preventDefault();
      first.focus();
    }
  }

  function setSubmenuState(item, isOpen) {
    if (!item) return;
    item.classList.toggle("is-submenu-open", isOpen);
    var submenuToggle = item.querySelector(":scope > .nav-drop-toggle");
    if (submenuToggle) submenuToggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
  }

  function closeSubmenus(header, exceptItem) {
    header.querySelectorAll(".nav-item.is-submenu-open").forEach(function (item) {
      if (item !== exceptItem) setSubmenuState(item, false);
    });
  }

  function closeMobileMenu(header, toggle) {
    header.classList.remove("is-menu-open");
    toggle.setAttribute("aria-expanded", "false");
    toggle.setAttribute("aria-label", "Open menu");
    closeSubmenus(header);
  }

  function setFormState(form, type, message) {
    var success = form.querySelector(".form-success");
    var error = form.querySelector(".form-error");
    if (success) success.style.display = type === "success" ? "block" : "none";
    if (error) error.style.display = type === "error" ? "block" : "none";
    if (type === "success" && success && message) success.textContent = message;
    if (type === "error" && error && message) error.textContent = message;
  }

  function isValidUsPhoneNumber(value) {
    var digits = String(value || "").replace(/\D/g, "");
    return digits.length === 10 || (digits.length === 11 && digits.charAt(0) === "1");
  }

  function validatePhoneField(form) {
    var phone = form.querySelector('input[name="phone"]');
    if (!phone) return true;

    phone.setCustomValidity("");
    if (isValidUsPhoneNumber(phone.value)) return true;

    var message = "Please enter a 10-digit U.S. phone number.";
    phone.setCustomValidity(message);
    phone.reportValidity();
    setFormState(form, "error", message);
    return false;
  }

  function cleanText(element) {
    if (!element) return "";
    var text = element.getAttribute("aria-label") || element.textContent || element.value || "";
    return text.replace(/\s+/g, " ").trim().slice(0, 120);
  }

  function createEventId(prefix) {
    return prefix + "_" + Date.now() + "_" + Math.random().toString(36).slice(2, 10);
  }

  function sanitizeAttributionValue(value, maxLength) {
    return String(value || "")
      .replace(/\s+/g, " ")
      .trim()
      .slice(0, maxLength || 1000);
  }

  function readStoredAttribution() {
    try {
      return JSON.parse(window.localStorage.getItem(attributionStorageKey) || "{}") || {};
    } catch (error) {
      return {};
    }
  }

  function writeStoredAttribution(attribution) {
    try {
      window.localStorage.setItem(attributionStorageKey, JSON.stringify(attribution));
    } catch (error) {
      // Storage can be unavailable in private or restricted browser contexts.
    }
  }

  function updateAttributionFromPage() {
    var stored = readStoredAttribution();
    var params = new URLSearchParams(window.location.search || "");
    var hasNewClickData = false;

    clickIdFieldNames.concat(utmFieldNames).forEach(function (fieldName) {
      var value = sanitizeAttributionValue(params.get(fieldName), 500);
      if (value) {
        stored[fieldName] = value;
        hasNewClickData = true;
      }
    });

    if (!stored.first_landing_page || hasNewClickData) {
      stored.first_landing_page = sanitizeAttributionValue(window.location.href, 1000);
    }

    if (!stored.referrer && document.referrer) {
      stored.referrer = sanitizeAttributionValue(document.referrer, 1000);
    }

    stored.landing_page = sanitizeAttributionValue(window.location.href, 1000);
    stored.attribution_updated_at = new Date().toISOString();
    currentAttribution = stored;
    writeStoredAttribution(stored);
    return stored;
  }

  function isQuoteForm(form) {
    if (!form) return false;
    var formName = [
      form.getAttribute("name"),
      form.getAttribute("data-name"),
      form.getAttribute("id"),
      form.className,
    ]
      .filter(Boolean)
      .join(" ")
      .toLowerCase();

    return formName.indexOf("quote") !== -1 || formName.indexOf("lead") !== -1;
  }

  function ensureSpamTrapFields(form) {
    if (!isQuoteForm(form)) return;

    if (!form.querySelector('input[name="website"]')) {
      var trap = document.createElement("label");
      trap.setAttribute("aria-hidden", "true");
      trap.style.cssText = "position:absolute;left:-10000px;top:auto;width:1px;height:1px;overflow:hidden;";
      trap.textContent = "Website";

      var trapInput = document.createElement("input");
      trapInput.setAttribute("type", "text");
      trapInput.setAttribute("name", "website");
      trapInput.setAttribute("tabindex", "-1");
      trapInput.setAttribute("autocomplete", "off");
      trap.appendChild(trapInput);
      form.appendChild(trap);
    }

    if (!form.querySelector('input[name="form-started-at"]')) {
      var startedAt = document.createElement("input");
      startedAt.setAttribute("type", "hidden");
      startedAt.setAttribute("name", "form-started-at");
      startedAt.value = String(Date.now());
      form.appendChild(startedAt);
    }

    if (!form.querySelector('input[name="submission-elapsed-ms"]')) {
      var elapsed = document.createElement("input");
      elapsed.setAttribute("type", "hidden");
      elapsed.setAttribute("name", "submission-elapsed-ms");
      form.appendChild(elapsed);
    }
  }

  function ensureHiddenField(form, fieldName) {
    var field = form.querySelector('input[name="' + fieldName + '"]');
    if (!field) {
      field = document.createElement("input");
      field.setAttribute("type", "hidden");
      field.setAttribute("name", fieldName);
      form.appendChild(field);
    }
    return field;
  }

  function ensureAttributionFields(form) {
    if (!isQuoteForm(form)) return;
    attributionFieldNames.forEach(function (fieldName) {
      ensureHiddenField(form, fieldName);
    });
    populateAttributionFields(form);
  }

  function populateAttributionFields(form) {
    if (!isQuoteForm(form)) return;
    var attribution = currentAttribution && Object.keys(currentAttribution).length ? currentAttribution : updateAttributionFromPage();

    attributionFieldNames.forEach(function (fieldName) {
      var field = ensureHiddenField(form, fieldName);
      field.value = sanitizeAttributionValue(attribution[fieldName], 1000);
    });
  }

  function updateSpamTrapTiming(form) {
    var startedAt = form.querySelector('input[name="form-started-at"]');
    var elapsed = form.querySelector('input[name="submission-elapsed-ms"]');
    if (!startedAt || !elapsed) return;

    var startedAtMs = Number.parseInt(startedAt.value || "0", 10);
    if (!startedAtMs) {
      startedAt.value = String(Date.now());
      elapsed.value = "";
      return;
    }

    elapsed.value = String(Math.max(0, Date.now() - startedAtMs));
  }

  function getSectionLabel(element) {
    var section = element.closest("header, footer, section, nav, [data-section], .hero-actions, .cta-actions, .form-actions");
    if (!section) return "";

    return (
      section.getAttribute("data-section") ||
      section.getAttribute("aria-label") ||
      (typeof section.className === "string" ? section.className.split(/\s+/).slice(0, 3).join(" ") : "") ||
      section.tagName.toLowerCase()
    );
  }

  function getCtaType(element) {
    var href = (element.getAttribute("href") || "").toLowerCase();
    var text = cleanText(element).toLowerCase();
    var type = (element.getAttribute("type") || "").toLowerCase();
    var form = element.form || element.closest("form");

    if ((type === "submit" || element.tagName.toLowerCase() === "button") && isQuoteForm(form)) {
      return "submit";
    }

    if (href.indexOf("tel:") === 0) return "call";
    if (href.indexOf("sms:") === 0) return "text";
    if (element.hasAttribute("data-open-quote") || href.indexOf("quote-form") !== -1) return "quote";
    if (/get (a )?quote|request.*quote|free quote|quote request|book.*clean|schedule/.test(text)) return "quote";

    return "";
  }

  function pushTrackingEvent(eventName, payload) {
    var data = {
      event: eventName,
      event_id: createEventId(eventName),
      event_timeout: 1500,
    };

    Object.keys(payload || {}).forEach(function (key) {
      data[key] = payload[key];
    });

    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push(data);
  }

  function trackCtaClick(element, ctaType) {
    pushTrackingEvent(ctaEventNames[ctaType], {
      cta_type: ctaType,
      cta_text: cleanText(element),
      cta_url: element.getAttribute("href") || "",
      cta_section: getSectionLabel(element),
      page_location: window.location.href,
      page_title: document.title,
      conversion_value: 1,
      currency: "USD",
    });
  }

  function handleCtaClick(event) {
    if (!event.target || typeof event.target.closest !== "function") return;

    var element = event.target.closest("a, button, input[type='submit']");
    if (!element) return;

    var ctaType = getCtaType(element);
    if (!ctaType || !ctaEventNames[ctaType]) return;

    trackCtaClick(element, ctaType);
  }

  function sendLeadConversionEvent(form) {
    var payload = {
      form_name: "Sun Ray Quote Request",
      lead_type: "quote_form",
      page_location: window.location.href,
      page_title: document.title,
      conversion_value: 1,
      currency: "USD",
    };

    clickIdFieldNames.concat(utmFieldNames).forEach(function (fieldName) {
      var field = form ? form.querySelector('input[name="' + fieldName + '"]') : null;
      var value = field ? field.value : currentAttribution[fieldName];
      if (value) payload[fieldName] = value;
    });

    pushTrackingEvent("sunray_lead_form_submit", payload);
  }

  function handleQuoteSubmit(event) {
    var form = event.currentTarget;
    var action = form.getAttribute("action");
    if (!action || action === "#") return;

    event.preventDefault();
    if (!validatePhoneField(form)) return;
    ensureSpamTrapFields(form);
    ensureAttributionFields(form);
    updateSpamTrapTiming(form);
    populateAttributionFields(form);
    var submitButton = form.querySelector('button[type="submit"]');
    var previousText = submitButton ? submitButton.textContent : "";
    setFormState(form, "", "");

    if (submitButton) {
      submitButton.disabled = true;
      submitButton.textContent = "Sending...";
    }

    fetch(action, {
      method: "POST",
      body: new FormData(form),
      headers: {
        accept: "application/json",
      },
    })
      .then(function (response) {
        return response.json().then(function (payload) {
          if (!response.ok || !payload.ok) {
            throw new Error(payload.message || "Please call or text (801) 604-2189 so we can help right away.");
          }
          return payload;
        });
      })
      .then(function (payload) {
        setFormState(form, "success", payload.message || "Thanks. Your quote request was received.");
        if (payload.trackConversion !== false) {
          sendLeadConversionEvent(form);
        }
        form.reset();
        var startedAt = form.querySelector('input[name="form-started-at"]');
        if (startedAt) startedAt.value = String(Date.now());
        populateAttributionFields(form);
      })
      .catch(function (error) {
        setFormState(form, "error", error.message || "Something went wrong. Please call or text (801) 604-2189.");
      })
      .finally(function () {
        if (submitButton) {
          submitButton.disabled = false;
          submitButton.textContent = previousText;
        }
      });
  }

  document.addEventListener("DOMContentLoaded", function () {
    updateAttributionFromPage();
    document.addEventListener("click", handleCtaClick, true);

    document.querySelectorAll(".site-header").forEach(function (header) {
      var toggle = header.querySelector(".nav-toggle");
      var nav = header.querySelector(".nav-links");
      if (!toggle || !nav) return;

      var mobileNav = window.matchMedia("(max-width: 1080px)");

      nav.querySelectorAll(".nav-drop-toggle").forEach(function (submenuToggle) {
        var item = submenuToggle.closest(".nav-item");
        submenuToggle.setAttribute("aria-haspopup", "true");
        submenuToggle.setAttribute("aria-expanded", "false");

        item.addEventListener("focusin", function () {
          submenuToggle.setAttribute("aria-expanded", "true");
        });

        item.addEventListener("focusout", function () {
          window.setTimeout(function () {
            if (!item.contains(document.activeElement) && !item.classList.contains("is-submenu-open")) {
              submenuToggle.setAttribute("aria-expanded", "false");
            }
          }, 0);
        });

        submenuToggle.addEventListener("click", function (event) {
          if (!mobileNav.matches) return;
          var isOpen = item.classList.contains("is-submenu-open");
          if (!isOpen) {
            event.preventDefault();
            closeSubmenus(header, item);
            setSubmenuState(item, true);
          }
        });
      });

      toggle.addEventListener("click", function () {
        var isOpen = header.classList.toggle("is-menu-open");
        toggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
        toggle.setAttribute("aria-label", isOpen ? "Close menu" : "Open menu");
        if (!isOpen) closeSubmenus(header);
      });

      nav.addEventListener("click", function (event) {
        var link = event.target.closest("a");
        if (!link || (mobileNav.matches && link.classList.contains("nav-drop-toggle") && event.defaultPrevented)) return;
        closeMobileMenu(header, toggle);
      });

      header.addEventListener("keydown", function (event) {
        if (event.key !== "Escape") return;
        var activeSubmenu = header.querySelector(".nav-item.is-submenu-open") || event.target.closest(".nav-item");
        if (activeSubmenu) {
          event.preventDefault();
          closeSubmenus(header);
          if (mobileNav.matches) {
            toggle.focus();
          } else if (document.activeElement && typeof document.activeElement.blur === "function") {
            document.activeElement.blur();
          }
          return;
        }
        if (header.classList.contains("is-menu-open")) {
          closeMobileMenu(header, toggle);
          toggle.focus();
        }
      });

      mobileNav.addEventListener("change", function (event) {
        if (!event.matches) closeMobileMenu(header, toggle);
      });
    });

    modal = document.querySelector("[data-quote-modal]");
    document.querySelectorAll(".quote-form").forEach(function (form) {
      ensureSpamTrapFields(form);
      ensureAttributionFields(form);
      var phone = form.querySelector('input[name="phone"]');
      if (phone) {
        phone.setAttribute("inputmode", "tel");
        phone.setAttribute("title", "Enter a 10-digit U.S. phone number");
        phone.addEventListener("input", function () {
          phone.setCustomValidity("");
        });
      }
      form.addEventListener("submit", handleQuoteSubmit);
    });

    if (!modal) return;

    document.querySelectorAll("[data-open-quote]").forEach(function (trigger) {
      trigger.addEventListener("click", openModal);
    });

    document.querySelectorAll("[data-close-quote]").forEach(function (trigger) {
      trigger.addEventListener("click", closeModal);
    });

    modal.addEventListener("click", function (event) {
      if (event.target === modal) closeModal();
    });

    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape" && modal.classList.contains("is-open")) closeModal();
      trapFocus(event);
    });
  });
})();
