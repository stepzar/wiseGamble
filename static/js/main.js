! function() { "use strict"; const e = (e, t = !1) => (e = e.trim(), t ? [...document.querySelectorAll(e)] : document.querySelector(e)),
        t = (t, i, s, o = !1) => { o ? e(i, o).forEach(e => e.addEventListener(t, s)) : e(i, o).addEventListener(t, s) },
        i = (e, t) => { e.addEventListener("scroll", t) }; let s = e("#navbar .scrollto", !0); const o = () => { let t = window.scrollY + 200;
        s.forEach(i => { if (!i.hash) return; let s = e(i.hash);
            s && (t >= s.offsetTop && t <= s.offsetTop + s.offsetHeight ? i.classList.add("active") : i.classList.remove("active")) }) };
    window.addEventListener("load", o), i(document, o); const l = t => { let i = e("#header"),
            s = i.offsetHeight;
        i.classList.contains("header-scrolled") || (s -= 10); let o = e(t).offsetTop;
        window.scrollTo({ top: o - s, behavior: "smooth" }) }; let a = e("#header"); if (a) { const e = () => { window.scrollY > 100 ? a.classList.add("header-scrolled") : a.classList.remove("header-scrolled") };
        window.addEventListener("load", e), i(document, e) } let n = e(".back-to-top"); if (n) { const e = () => { window.scrollY > 100 ? n.classList.add("active") : n.classList.remove("active") };
        window.addEventListener("load", e), i(document, e) }
    t("click", ".mobile-nav-toggle", function(t) { e("#navbar").classList.toggle("navbar-mobile"), this.classList.toggle("bi-list"), this.classList.toggle("bi-x") }), t("click", ".navbar .dropdown > a", function(t) { e("#navbar").classList.contains("navbar-mobile") && (t.preventDefault(), this.nextElementSibling.classList.toggle("dropdown-active")) }, !0), t("click", ".scrollto", function(t) { if (e(this.hash)) { t.preventDefault(); let i = e("#navbar"); if (i.classList.contains("navbar-mobile")) { i.classList.remove("navbar-mobile"); let t = e(".mobile-nav-toggle");
                t.classList.toggle("bi-list"), t.classList.toggle("bi-x") }
            l(this.hash) } }, !0), window.addEventListener("load", () => { window.location.hash && e(window.location.hash) && l(window.location.hash) }), new Swiper(".clients-slider", { speed: 400, loop: !0, autoplay: { delay: 5e3, disableOnInteraction: !1 }, slidesPerView: "auto", pagination: { el: ".swiper-pagination", type: "bullets", clickable: !0 }, breakpoints: { 320: { slidesPerView: 2, spaceBetween: 40 }, 480: { slidesPerView: 3, spaceBetween: 60 }, 640: { slidesPerView: 4, spaceBetween: 80 }, 992: { slidesPerView: 6, spaceBetween: 120 } } }), window.addEventListener("load", () => { let i = e(".portfolio-container"); if (i) { let s = new Isotope(i, { itemSelector: ".portfolio-item", layoutMode: "fitRows" }),
                o = e("#portfolio-flters li", !0);
            t("click", "#portfolio-flters li", function(e) { e.preventDefault(), o.forEach(function(e) { e.classList.remove("filter-active") }), this.classList.add("filter-active"), s.arrange({ filter: this.getAttribute("data-filter") }), r() }, !0) } });
    GLightbox({ selector: ".portfokio-lightbox" });

    function r() { AOS.init({ duration: 1e3, easing: "ease-in-out", once: !0, mirror: !1 }) }
    new Swiper(".portfolio-details-slider", { speed: 400, autoplay: { delay: 5e3, disableOnInteraction: !1 }, pagination: { el: ".swiper-pagination", type: "bullets", clickable: !0 } }), new Swiper(".testimonials-slider", { speed: 600, loop: !0, autoplay: { delay: 5e3, disableOnInteraction: !1 }, slidesPerView: "auto", pagination: { el: ".swiper-pagination", type: "bullets", clickable: !0 }, breakpoints: { 320: { slidesPerView: 1, spaceBetween: 40 }, 1200: { slidesPerView: 3 } } }), window.addEventListener("load", () => { r() }) }();