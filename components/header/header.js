class Header {
  render(){
    const html = `
        <div class="header">
          <div class="header__field">
            <div class="header__content">
              <div class="header__menu">
                <a class="header__menu-a" href="index.html">ДОМ</a>
                <a class="header__menu-a" href="our-services.html">СЕРВИСЫ</a>
                <a class="header__menu-a" href="our-portfolio.html">СЕМЬЯ</a>
                <a class="header__menu-a header__menu-a_logo" href="index.html">WAMUU</a>
                <a class="header__menu-a" href="team.html">НАША КОМАНДА</a>
                <a class="header__menu-a" href="blog.html">АНЕКДОТЫ</a>
                <a class="header__menu-a" href="contact-us.html">КОНТАКТЫ</a>
              </div>
            </div>
          </div>
        </div>
      `;

      ROOT_HEADER.insertAdjacentHTML('afterbegin', html);
  }
}

const headerPage = new Header();
headerPage.render();
