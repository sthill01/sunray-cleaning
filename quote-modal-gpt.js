(function () {
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

  function sendLeadConversionEvent() {
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({
      event: "sunray_lead_form_submit",
      form_name: "Sun Ray Quote Request",
      lead_type: "quote_form",
    });

    if (window.google_tag_manager || typeof window.gtag !== "function") return;

    try {
      window.gtag("event", "conversion_event_submit_lead_form_1", {
        event_timeout: 2000,
      });
    } catch (error) {
      // Tracking should never interrupt the quote form experience.
    }
  }

  function handleQuoteSubmit(event) {
    var form = event.currentTarget;
    var action = form.getAttribute("action");
    if (!action || action === "#") return;

    event.preventDefault();
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
        sendLeadConversionEvent();
        form.reset();
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
    modal = document.querySelector("[data-quote-modal]");
    document.querySelectorAll(".quote-form").forEach(function (form) {
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
