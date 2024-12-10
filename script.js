document.addEventListener('DOMContentLoaded', () => {
    // Cargar el archivo JSON automáticamente cuando la página se carga
    fetch('data/series.json')  // Ruta del archivo JSON en tu servidor local
        .then(response => response.json())  // Parsear el JSON
        .then(data => {
            const seriesList = document.getElementById('series-list');
            
            // Iterar sobre las series del JSON
            for (const serieName in data) {
                if (data.hasOwnProperty(serieName)) {
                    const serie = data[serieName];
                    const serieItem = document.createElement('li');
                    serieItem.textContent = serieName;
                    const episodeList = document.createElement('ul');

                    // Iterar sobre los episodios de cada serie
                    serie.episodios.forEach((episodio, index) => {
                        const episodioItem = document.createElement('li');
                        // Mostrar el número y nombre del episodio
                        episodioItem.textContent = ` ${episodio.numero}: ${episodio.nombre}`;
                        
                        // Si el episodio es una OVA o una Película, lo indicamos
                        if (episodio.tipo) {
                            const tipoSpan = document.createElement('span');
                            tipoSpan.textContent = ` (${episodio.tipo})`;
                            episodioItem.appendChild(tipoSpan);
                        }

                        // Crear la casilla de verificación
                        const checkbox = document.createElement('input');
                        checkbox.type = 'checkbox';
                        // Leer el estado desde localStorage o el valor por defecto (false)
                        const storedState = localStorage.getItem(`serie_${serieName}_episodio_${index}`);
                        checkbox.checked = storedState === 'true';  // Verificar si el episodio fue marcado previamente

                        // Agregar un evento para guardar el estado en localStorage cuando el checkbox cambie
                        checkbox.addEventListener('change', () => {
                            localStorage.setItem(`serie_${serieName}_episodio_${index}`, checkbox.checked);
                        });

                        episodioItem.appendChild(checkbox);
                        episodeList.appendChild(episodioItem);
                    });

                    // Añadir la lista de episodios al elemento de la serie
                    serieItem.appendChild(episodeList);
                    seriesList.appendChild(serieItem);
                }
            }
        })
        .catch(error => console.error('Error al cargar el JSON:', error));
});
