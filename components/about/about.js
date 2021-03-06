class About {
  render(){
    const html = `
        <div class="homepage-about">
          <div class="homepage-about__field">
            <div class="homepage-about__content">
              <div class="homepage-about__info">
                <h2 class="homepage-about__h2">Что любит Шлёпа?</h2>
                <div class="homepage-about__partition"></div>
                <!-- <p class="homepage-about__text">Nunc ac lorem vel arcu ultricies volutpat at nec arcu. Ut tempus dignissim est, at iaculis massa blandit commodo. In vitae nunc eget arcu aliquam hendrerit a vel dui. Aliquam a sagittis neque, nec congue eros.</p> -->
              </div>
              <div class="homepage-about__points">
                <div class="homepage-about__point">
                  <svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" viewBox="0 0 50 50">
                    <defs>
                      <style>
                        .cls-1 {
                          fill-rule: evenodd;
                        }
                      </style>
                    </defs>
                    <path id="chart" class="cls-1" d="M9,9h1V40H41v1H9V9Zm4,19.99h2V39H13V28.99ZM19,26h2V39H19V26Zm6-4h2V39H25V22Zm6-6h2V39.062H31V16Zm6,11h2V39H37V27Z"/>
                  </svg>
                  <p>Торговать</p>
                </div>
                <div class="homepage-about__point">
                  <svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" viewBox="0 0 50 50">
                    <defs>
                      <style>
                        .cls-1 {
                          fill-rule: evenodd;
                        }
                      </style>
                    </defs>
                    <path id="location_pin" data-name="location pin" class="cls-1" d="M25,41S13.031,34.031,13.031,22c0-4.969,1.841-13,11.969-13,10.1,0,11.969,7,11.969,13C36.969,34.094,25,41,25,41Zm0-23.969a3.984,3.984,0,1,1-4,3.985A3.992,3.992,0,0,1,25,17.031ZM25,19a2,2,0,1,1-2,2A2,2,0,0,1,25,19Zm0,19.758S14.708,32.7,14.708,22.235c0-4.321,1.583-11.305,10.292-11.305,8.683,0,10.292,6.087,10.292,11.305C35.291,32.752,25,38.758,25,38.758Z"/>
                  </svg>
                  <p>Свою страну</p>
                </div>
                <div class="homepage-about__point">
                  <svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" viewBox="0 0 50 50">
                    <defs>
                      <style>
                        .cls-1 {
                          fill-rule: evenodd;
                        }
                      </style>
                    </defs>
                    <path id="map" class="cls-1" d="M21.125,8L32.05,12.375V43L21.125,39.719V8Zm0,2.188,8.75,3.281V40.375l-8.75-2.844V10.187ZM8,13L21.138,8V39L8,43V13Zm2.18,1.563,8.765-3.281v26.25L10.18,40.375V14.562Zm21.883-2.188L43,8V38.625L32.062,43V12.375Zm0,2.188,8.75-3.281v26.25l-8.75,3.281V14.562Z"/>
                  </svg>
                  <p>Анекдоты</p>
                </div>
                <div class="homepage-about__point">
                  <svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" viewBox="0 0 50 50">
                    <defs>
                      <style>
                        .cls-1 {
                          fill-rule: evenodd;
                        }
                      </style>
                    </defs>
                    <path id="list" class="cls-1" d="M13,21.008a4,4,0,1,1-4,4A4,4,0,0,1,13,21.008Zm0,1.613a2.389,2.389,0,1,1-2.388,2.389A2.388,2.388,0,0,1,13,22.621Zm8,1.442V26H41V24.062H21Zm0-12V14H41V12.062H21Zm-0.063,24V38H41V36.062H20.937ZM13,33.008a4,4,0,1,1-4,4A4,4,0,0,1,13,33.008Zm0,1.613a2.389,2.389,0,1,1-2.388,2.389A2.388,2.388,0,0,1,13,34.621ZM13,9.008a4,4,0,1,1-4,4A4,4,0,0,1,13,9.008Zm0,1.613a2.389,2.389,0,1,1-2.388,2.389A2.388,2.388,0,0,1,13,10.621Z"/>
                  </svg>
                  <p>Семью</p>
                </div>
                <div class="homepage-about__point">
                  <svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" viewBox="0 0 50 50">
                    <defs>
                      <style>
                        .cls-1 {
                          fill-rule: evenodd;
                        }
                      </style>
                    </defs>
                    <path id="user" class="cls-1" d="M41,41H9s0-8.031,6-8.031,7-1.3,7-1.721S22,30,22,30h6s0,0.915,0,1.248,0.938,1.721,6.969,1.721C41.093,32.969,41,41,41,41Zm-3-1.969H12s0-4,4-4c5.256,0,8-1.51,8-2.817V30h2v2.214c0,1.474,2.717,2.817,8,2.817C38,35.031,38,39.031,38,39.031ZM25,9c4.418,0,8,4.7,8,10.5S29.418,30,25,30s-8-4.7-8-10.5S20.582,9,25,9Zm-0.016,2.031c3.305,0,5.984,3.806,5.984,8.5s-2.679,8.5-5.984,8.5S19,24.226,19,19.531,21.679,11.031,24.984,11.031Z"/>
                  </svg>
                  <p>Пользователей</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      `;

      ROOT_ABOUT.insertAdjacentHTML('afterbegin', html);
  }
}

const aboutPage = new About();
aboutPage.render();
