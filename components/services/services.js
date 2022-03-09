class Services {
  render(){
    const html = `
        <main>
          <div class="main__content">
            <div class="main__head">Наши сервисы</div>
            <div class="main__separator"></div>
            <div class="main__after-head">
              На даной странице вы можете узнать что вы можете делать на данном сайте, наслаждайтесь.
            </div>
            <div class="main__two-column">
              <div class="main__two-column__element">
                <div class="main__two-column__element__image">
                  <img src="img/our-services/user.png">
                </div>
                <h3>Мы заботимся о наших пользователях</h3>
                <p>Пользователям оказывается постоянная круглосуточная поддержка. При возниковении любой непредвиденной ситуации вы можете обратится в нашу службу поддержки.</p>
              </div>
              <div class="main__two-column__element">
                <div class="main__two-column__element__image">
                  <img src="img/our-services/bubble.png">
                </div>
                <h3>Комментарии</h3>
                <p>Вы можете свободно оставлять комментарии. Мы будем рады если вы честно поделится своим мнением. Неподобающие сообщения будут удалены. Будьте снисходительны друг к другу.</p>
              </div>
              <div class="main__two-column__element">
                <div class="main__two-column__element__image">
                  <img src="img/our-services/headphones.png">
                </div>
                <h3>Наушники</h3>
                <p>Наденьте наушники для более захватывающего пользовательского опыта. Использование наушников позволяет получать более качественное звучание.</p>
              </div>
              <div class="main__two-column__element">
                <div class="main__two-column__element__image">
                  <img src="img/our-services/pencil.png">
                </div>
                <h3>Анекдоты</h3>
                <p>Почувтствуйте силу АНЕКДОТОВ! На  сайте представлены лучшие анекдоты со всего мира. Также вы можете самостоятельно сочинить и выложить на всеобщее обозрение свой собственный анекдот.</p>
              </div>
              <div class="main__two-column__element">
                <div class="main__two-column__element__image">
                  <img src="img/our-services/message.png">
                </div>
                <h3>Почта</h3>
                <p>При регистрации на сайте используется ваша почта. Также вы можете получать уведомления об обновлениях сайта на почту.</p>
              </div>
              <div class="main__two-column__element">
                <div class="main__two-column__element__image">
                  <img src="img/our-services/sunny.png">
                </div>
                <h3>Яркость</h3>
                <p>Вы можете настроить яркость на нашем сайте с высокой точностью. Больше не чуствуйте боль в глазах при ночной работе.</p>
              </div>
              <div class="main__two-column__element">
                <div class="main__two-column__element__image">
                  <img src="img/our-services/musical note.png">
                </div>
                <h3>Музыка</h3>
                <p>Во время работы на нашем сайте вы можете слушать свою любимую музыку. Наслаждайтесь приятным времяпрепровождением.</p>
              </div>
              <div class="main__two-column__element">
                <div class="main__two-column__element__image">
                  <img src="img/our-services/padlock.png">
                </div>
                <h3>Шифрование</h3>
                <p>На нашем сайте используются самые современные методы шифрования. Ваши пароли и личная информация в безопасности.</p>
              </div>
            </div>
          </div>
        </main>
      `;

      ROOT_SERVICES.insertAdjacentHTML('afterbegin', html);
  }
}

const servicesPage = new Services();
servicesPage.render();
