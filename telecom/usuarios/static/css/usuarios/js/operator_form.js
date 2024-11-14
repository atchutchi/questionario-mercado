// usuarios/static/js/operator_form.js
document.addEventListener('DOMContentLoaded', function() {
    // Inicializa o form com dados existentes do contato técnico
    const technicalContactInput = document.querySelector('#id_technical_contact');
    const technicalContactData = technicalContactInput ? JSON.parse(technicalContactInput.value || '{}') : {};

    if (technicalContactData) {
        document.querySelector('[name="tech_contact_name"]').value = technicalContactData.name || '';
        document.querySelector('[name="tech_contact_email"]').value = technicalContactData.email || '';
        document.querySelector('[name="tech_contact_phone"]').value = technicalContactData.phone || '';
    }

    // Atualiza o campo hidden do technical_contact antes do submit
    document.querySelector('form').addEventListener('submit', function(e) {
        const technicalContact = {
            name: document.querySelector('[name="tech_contact_name"]').value,
            email: document.querySelector('[name="tech_contact_email"]').value,
            phone: document.querySelector('[name="tech_contact_phone"]').value
        };
        document.querySelector('#id_technical_contact').value = JSON.stringify(technicalContact);
    });
});