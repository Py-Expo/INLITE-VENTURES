class StickyNav {
    constructor() {
      this.curId = this.curSect = null;
      this.navbarHeight = $(".nav-bar").height();
  
      $(".nav-link").click((e) => {
        e.preventDefault();
        let el = $(e.currentTarget);
        let scroll = $(el.attr("href")).offset().top - this.navbarHeight + 1;
        $("html, body").animate({ scrollTop: scroll }, 400);
      });
      $(window).scroll(() => this.onScroll());
      $(window).resize(() => this.onResize());
    }
  
    onScroll() {
      this.checkNavbar();
      this.findPosition();
    }
    onResize() {
      if (this.curId) this.updateSlider();
    }
  
    checkNavbar() {
      let off = $(".nav").offset().top + $(".nav").height() - this.navbarHeight;
      if ($(window).scrollTop() > off) {
        $(".nav-bar").addClass("nav-bar-fixed");
      } else {
        $(".nav-bar").removeClass("nav-bar-fixed");
      }
    }
  
    findPosition() {
      let newId, newSect;
      $(".nav-link").each((i, el) => {
        let id = $(el).attr("href");
        let top = $(id).offset().top - this.navbarHeight;
        let bot = $(id).offset().top + $(id).height() - this.navbarHeight;
        let scroll = $(window).scrollTop();
        if (scroll > top && scroll < bot) {
          newId = id;
          newSect = $(el);
        }
      });
      if (!this.curId || this.curId != newId) {
        this.curId = newId;
        this.curSect = newSect;
        this.updateSlider();
      }
    }
  
    updateSlider() {
      let width = 0,
        left = 0;
      if (this.curId) {
        width = this.curSect.css("width");
        left = this.curSect.offset().left;
      }
      $(".nav-slider").css("width", width);
      $(".nav-slider").css("left", left);
    }
  }
  
  new StickyNav();
  