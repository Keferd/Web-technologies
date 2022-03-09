class Blog {
  render(){
    const html = `
        <div class="blog__content">

          <div class="blog__content_fs1">
            <p>Внимание! Анекдот</p>
          </div>
          <div class="blog__content_separete">

          </div>
          <div class="blog__content_fs2">
            <p>
              Сталкер — одна из самых «народных» игр на постсоветском пространстве.
               Об этом говорит и популярность различных пользовательских модификаций,
               и бурная реакцию на каждый новый тизер второй части серии.
               Сегодня даже анекдоты, которые рассказывали сталкеры у костра и в баре, вызывают чувство ностальгии.
               Лучшие из них мы собрали в этой статье.
            </p>
            <br>

            <div class="blog__pages">
              <div class="blog__content-block">
                <img class="blog__content-image" src="img/blog/Gregory.png" alt="Shlepa">
                <p style="font-weight:bold;">Появился, значит, в Зоне Чёрный сталкер.</p>
                <br>
                <p>Появился, значит, в Зоне Чёрный сталкер. К лагерю ночью повадился ходить и там сует руку в палатку и говорит: «Водички попить!»
                </p>
                <br>
                <!-- <a href="blogpost.html">Read more</a> -->
              </div>
              <div class="blog__content-block">
                <img class="blog__content-image" src="img/blog/Gregory.png" alt="Shlepa">
                <p style="font-weight:bold;">Долг и свобода</p>
                <br>
                <p>Встречаются двое сталкеров, ну и один говорит:
                  — На днях к Долгу заходил…
                  — Ну и?
                  — Что и? И остался должен. Ха. А потом

                </p>
                <br>
                <!-- <a href="blogpost.html">Read more</a> -->
              </div>
              <div class="blog__content-block">
                <img class="blog__content-image" src="img/blog/Gregory.png" alt="Shlepa">
                <p style="font-weight:bold;">Сталкер и доктор</p>
                <br>
                <p>Сталкер пришел к доктору и говорит:
                  — Доктор, я совсем не могу спать… Мне снится, будто я заперт в саркофаге…
                </p>
                <br>
                <!-- <a href="blogpost.html">Read more</a> -->
              </div>
              <div class="blog__content-block">
                <img class="blog__content-image" src="img/blog/Gregory.png" alt="Shlepa">
                <p style="font-weight:bold;">Заблудившийся</p>
                <br>
                <p>Заблудился как-то долговец и кричит:— Люди, отзовитесь, кто-нибудь! Аууу! Тут его кто то догоняет и…
                </p>
                <br>
                <!-- <a href="blogpost.html">Read more</a> -->
              </div>
              <div class="blog__content-block">
                <img class="blog__content-image" src="img/blog/Gregory.png" alt="Shlepa">
                <p style="font-weight:bold;">Ходячая аномалия</p>
                <br>
                <p>Бродит, говорят, по зоне ходячая аномалия — непьющий и некурящий сталкер.
                </p>
                <br>
                <!-- <a href="blogpost.html">Read more</a> -->
              </div>
              <div class="blog__content-block">
                <img class="blog__content-image" src="img/blog/Gregory.png" alt="Shlepa">
                <p style="font-weight:bold;">Признание</p>
                <br>
                <p>У блок-поста прихватили новичка-сталкера и давай пытать:— С какой целью вы пытались проникнуть
                </p>
                <br>
                <!-- <a href="blogpost.html">Read more</a> -->
              </div>
          </div>
          </div>

        </div>
      `;

      ROOT_BLOG.insertAdjacentHTML('afterbegin', html);
  }
}

const blogPage = new Blog();
blogPage.render();
