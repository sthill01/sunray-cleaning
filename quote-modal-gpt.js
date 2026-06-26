(function () {
  var ctaEventNames = {
    quote: "sunray_quote_cta_click",
    call: "sunray_call_cta_click",
    text: "sunray_text_cta_click",
    submit: "sunray_quote_submit_click",
  };
  var modal;
  var lastFocused;

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

  function setFormState(form, type, message) {
    var success = form.querySelector(".form-success");
    var error = form.querySelector(".form-error");
    if (success) success.style.display = type === "success" ? "block" : "none";
    if (error) error.style.display = type === "error" ? "block" : "none";
    if (type === "success" && success && message) success.textContent = message;
    if (type === "error" && error && message) error.textContent = message;
  }

  function cleanText(element) {
    if (!element) return "";
    var text = element.getAttribute("aria-label") || element.textContent || element.value || "";
    return text.replace(/\s+/g, " ").trim().slice(0, 120);
  }

  function createEventId(prefix) {
    return prefix + "_" + Date.now() + "_" + Math.random().toString(36).slice(2, 10);
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

  function sendLeadConversionEvent() {
    pushTrackingEvent("sunray_lead_form_submit", {
      form_name: "Sun Ray Quote Request",
      lead_type: "quote_form",
      page_location: window.location.href,
      page_title: document.title,
      conversion_value: 1,
      currency: "USD",
    });
  }

  function handleQuoteSubmit(event) {
    var form = event.currentTarget;
    var action = form.getAttribute("action");
    if (!action || action === "#") return;

    event.preventDefault();
    ensureSpamTrapFields(form);
    updateSpamTrapTiming(form);
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
          sendLeadConversionEvent();
        }
        form.reset();
        var startedAt = form.querySelector('input[name="form-started-at"]');
        if (startedAt) startedAt.value = String(Date.now());
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
    document.addEventListener("click", handleCtaClick, true);

    modal = document.querySelector("[data-quote-modal]");
    document.querySelectorAll(".quote-form").forEach(function (form) {
      ensureSpamTrapFields(form);
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
