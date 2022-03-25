class Team {
  render(){
    const html = `
    <div class="team">
      <div class="team__field">
        <div class="team__content">
          <div class="team__info">
            <h1 class="team__h1">Наша команда</h2>
            <div class="team__partition"></div>
            <p class="team__text">Nunc ac lorem vel arcu ultricies volutpat at nec arcu. Ut tempus dignissim est, at iaculis massa blandit commodo. In vitae nunc eget arcu aliquam hendrerit a vel dui. Aliquam a sagittis neque, nec congue eros.</p>
          </div>
          <div class="team__">
          <table class="team__table" border="1" id="team-table">
            <caption>Состав команды</caption>
            <tr>
              <th onclick="team_table_sort(0)">№</th>
              <th onclick="team_table_sort(1)">Имя</th>
              <th onclick="team_table_sort2(2)">Фамилия</th>
              <th onclick="team_table_sort2(3)">Другое</th>
            </tr>
            <tr>
              <td>1</td>
              <td>3</td>
              <td>4</td>
              <td>2</td>
            </tr>
            <tr>
              <td>2</td>
              <td>2</td>
              <td>5</td>
              <td>5</td>
            </tr>
            <tr>
              <td>3</td>
              <td>4</td>
              <td>3</td>
              <td>4</td>
            </tr>
            <tr>
              <td>4</td>
              <td>5</td>
              <td>2</td>
              <td>3</td>
            </tr>
          </table>
          </div>
        </div>
      </div>
    </div>
      `;

      ROOT_TEAM.insertAdjacentHTML('afterbegin', html);
  }
}

const teamPage = new Team();
teamPage.render();
