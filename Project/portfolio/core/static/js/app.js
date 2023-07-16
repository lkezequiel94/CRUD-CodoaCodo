const $form = document.querySelector('#form');
const currentView = document.body.getAttribute("data-active");
const link = document.getElementById(`link-${currentView}`);

    if (link) {
        link.classList.add("active");
    }

  $form.addEventListener('submit', handleSubmit);

  async function handleSubmit(event) {
    event.preventDefault(); // Evita que el formulario se envíe al sitio de Formspree
    const form = new FormData(this);
    const response = await fetch(this.action, {
      method: this.method,
      body: form,
      headers: {
        'Accept': 'application/json'
      }
    });
    if (response.ok) {
      this.reset();
      alert('Gracias por contactarme, pronto estaré respondiéndote');
    }
  }