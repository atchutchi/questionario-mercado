document.addEventListener('DOMContentLoaded', function() {
    // Previne que o link principal do submenu redirecione
    document.querySelectorAll('.dropdown-submenu > a').forEach(function(element) {
        element.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
        });
    });
});