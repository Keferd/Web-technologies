class Contact_us {
  render(){
    const html = `
        <div class="contact-us">
          <div class="contact-us__field">
            <div class="contact-us__content">
              <div class="contact-us__info">
                <h1 class="contact-us__h1">Что любит Шлёпа?</h2>
                <div class="contact-us__partition"></div>
                <p class="contact-us__text">Nunc ac lorem vel arcu ultricies volutpat at nec arcu. Ut tempus dignissim est, at iaculis massa blandit commodo. In vitae nunc eget arcu aliquam hendrerit a vel dui. Aliquam a sagittis neque, nec congue eros.</p>
              </div>
              <div class="contact-us__columns">
                <div class="contact-us__column">
                  <h2 class="contact-us__column-h2">Feel free to drop us a line</h2>
                  <p class="contact-us__column-p">Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. </p>
                  <form class="contact-us__form">
                    <input class="contact-us__input-text" type="text" placeholder="Full name" required>
                    <input class="contact-us__input-text" type="text" placeholder="E-mail address" required>
                    <textarea class="contact-us__textarea" placeholder="Message" required></textarea>
                    <input class="contact-us__input-submit" type="submit" onclick="Сontact_UsConfirmDialog()">
                  </form>
                </div>
                <div class="contact-us__column">
                  <h2 class="contact-us__column-h2">Address</h2>
                  <p class="contact-us__column-p">Sed facilisis non ipsum et interdum. Suspendisse pretium magna sed auctor dictum. Quisque non dignissim metus, non eleifend mi.</p>

                  <p class="contact-us__address">
                    An address here, 100/2<br>
                    Cityname, 20123<br>
                    Country<br>
                    P: (0) 123 456 789<br>
                    E: info@wdsinc.com
                  </p>

                  <div id="contact-us__map" class="contact-us__map"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      `;

      ROOT_CONTACTUS.insertAdjacentHTML('afterbegin', html);
  }
}

const contact_usPage = new Contact_us();
contact_usPage.render();
