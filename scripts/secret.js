class Secret {
    constructor(element) {
        this.mount(element);
    }

    mount(element) {
        this.container = document.createElement('div');
        document.body.appendChild(this.container);
        this.container.innerHTML = this.render(this.randomInteger(1,2));
        element.insertAdjacentElement('beforeend', this.container);
        setTimeout(() => { this.destroy(); }, 500);
    }

    randomInteger(min, max) {
        let rand = min + Math.random() * (max + 1 - min);
        return Math.floor(rand);
    }

    destroy() {
        this.container.remove();
    }

   render(a) {
        return `
      <div class="secret">
      </div>
      <style>
        .secret {
          background-color: black;
          position: fixed;
          left: 0;
          top: 0;
          height: 100%;
          width: 100%;
          background-image: url('img/secret/${a}.png');
          background-repeat: no-repeat;
          background-size: contain;
          background-position: center;
          opacity: 0;

          animation-duration: 0.5s;
          animation-name: secret;
        }

        @keyframes secret {
          0% {
              opacity: 1;
          }

          20% {
              opacity: 0.5;
          }

          100% {
              opacity: 0;
          }
        }
      </style>
      `
    }
}

document.querySelector('#homepage__secret').addEventListener(
            'click', (e) => { const secret = new Secret(document.body);  }
       );
console.log('hello');
