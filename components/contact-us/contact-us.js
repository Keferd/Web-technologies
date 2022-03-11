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
              <div class="contact-us__">
                <div>
                  <h2></h2>
                  <p></p>
                  <form>
                    <input type="text">
                    <input type="text">
                    <textarea></textarea>
                    <input type="submit">
                  </form>
                </div>
                <div>
                  <h2></h2>
                  <p></p>

                  <p></p>
                  <p></p>
                  <p></p>
                  <p></p>
                  <p></p>

                  <div></div>
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
