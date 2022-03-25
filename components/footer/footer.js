class Footer {
  render(){
    const html = `
        <div class="footer">
          <div class="footer__field">
            <div class="footer__content">
              <div class="footer__social-media">
                <a class="footer__sm-logo footer__sm-logo_twitter"></a>
                <a class="footer__sm-logo footer__sm-logo_facebook"></a>
                <a class="footer__sm-logo footer__sm-logo_google"></a>
                <a class="footer__sm-logo footer__sm-logo_pinterest"></a>
                <a class="footer__sm-logo footer__sm-logo_rss"></a>
              </div>
              <div class="footer__rights">
                <p>© 2014 WebDesign Studio. All rights reserved.</p>
                <p>Designed and developed by pcklab.com</p>
              </div>
            </div>
          </div>
        </div>
      `;

      ROOT_FOOTER.insertAdjacentHTML('afterbegin', html);
  }
}

const footerPage = new Footer();
footerPage.render();
