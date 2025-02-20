// Deshabilitar clic derecho
document.addEventListener('contextmenu', function(e) {
    e.preventDefault();
});

// Deshabilitar teclas como F12, Ctrl+Shift+I, Ctrl+U, y Ctrl+Shift+C para evitar abrir DevTools
document.addEventListener('keydown', function(e) {
    if (
        e.key === "F12" || 
        (e.ctrlKey && e.shiftKey && e.key === 'I') || 
        (e.ctrlKey && e.key === 'u') || 
        (e.ctrlKey && e.shiftKey && e.key === 'C') || 
        (e.key === 'PrintScreen') || 
        (e.ctrlKey && e.shiftKey && e.key === 'S') || 
        (e.ctrlKey && e.key === 'S') || 
        (e.ctrlKey && e.key === 'P')
    ) {
        e.preventDefault();
    }
});

// Deshabilitar Print Screen key (Impr Pant)
document.addEventListener('keyup', function(e) {
    if (e.key === 'PrintScreen') {
        navigator.clipboard.writeText('');
    }
});

// Evitar que los usuarios graben la pantalla con un segundo dispositivo (Ejemplo, idea conceptual)
setInterval(function(){
    console.log('Verificación periódica para proteger contenido.');
}, 3000);
