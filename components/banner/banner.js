class Banner {
  render(){
    const html = `
        <div class="homepage-banner">
          <div class="homepage-banner__field">
            <div class="homepage-banner__content">
              <div class="homepage-banner__area homepage-banner__area_upper">
                <div class="homepage-banner__text-over">
                  <div class="homepage-banner__dot"></div>
                  <div class="homepage-banner__">Большой русский кот</div>
                  <div class="homepage-banner__dot"></div>
                </div>
                <h1 class="homepage-banner__h1">Сайт имени кота Шлёпы</h1>
                <div class="homepage-banner__text-under">
                  <div class="homepage-banner__lines"></div>
                  <div>
                    Всем добра!
                  </div>
                  <div class="homepage-banner__lines"></div>
                </div>
              </div>
              <div class="homepage-banner__area">
                <div class="homepage-banner__button">Нажмите сюда</div>
              </div>
            </div>
          </div>
        </div>
      `;

      ROOT_BANNER.insertAdjacentHTML('afterbegin', html);
  }
}

const bannerPage = new Banner();
bannerPage.render();
