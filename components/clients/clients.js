class Clients {
  render(){
    const html = `
        <div class="homepage-clients">
          <div class="homepage-clients__field">
            <div class="homepage-about__content">
              <div class="homepage-about__info">
                <h2 class="homepage-about__h2">Кто работает с Шлёпой?</h2>
                <div class="homepage-about__partition"></div>
                <!-- <p class="homepage-about__text">Duis posuere sollicitudin felis, sit amet tempus orci iaculis eu. Donec quis laoreet dolor. Nam sed mi nisl. Duis ultricies lacus nec auctor rhoncus. Praesent quis tincidunt orci.</p> -->
              </div>
              <div class="homepage-clients__our-clients">
                <div class="homepage-clients__arrow">
                  <svg
                   xmlns="http://www.w3.org/2000/svg"
                   xmlns:xlink="http://www.w3.org/1999/xlink"
                   width="14px" height="23px">
                    <path fill-rule="evenodd"  fill="rgb(0, 0, 0)"
                     d="M11.394,22.949 L-0.001,11.475 L11.394,0.001 L14.001,2.589 L5.176,11.475 L14.001,20.360 L11.394,22.949 Z"/>
                  </svg>
                </div>

                <div class="homepage-clients__clients">
                  <div class="homepage-clients__client">
                    <img src="img/clients/mountains-solution.png" alt="">
                  </div>
                  <div class="homepage-clients__client">
                    <img src="img/clients/bow-tie.png" alt="">
                  </div>
                  <div class="homepage-clients__client">
                    <img src="img/clients/beautiful-spiral.png" alt="">
                  </div>
                  <div class="homepage-clients__client">
                    <img src="img/clients/circle-me.png" alt="">
                  </div>
                  <div class="homepage-clients__client">
                    <img src="img/clients/crossing-lines.png" alt="">
                  </div>
                </div>

                <div class="homepage-clients__arrow">
                  <svg
                   xmlns="http://www.w3.org/2000/svg"
                   xmlns:xlink="http://www.w3.org/1999/xlink"
                   width="14px" height="23px">
                    <path fill-rule="evenodd"  fill="rgb(0, 0, 0)"
                     d="M2.606,22.949 L14.001,11.475 L2.606,0.001 L-0.001,2.589 L8.824,11.475 L-0.001,20.360 L2.606,22.949 Z"/>
                  </svg>
                </div>
              </div>
            </div>
          </div>
        </div>
      `;

      ROOT_CLIENTS.insertAdjacentHTML('afterbegin', html);
  }
}

const clientsPage = new Clients();
clientsPage.render();
