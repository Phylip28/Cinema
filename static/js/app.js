document.addEventListener('DOMContentLoaded', () => {
    const movieForm = document.getElementById('movie-form');
    const movieList = document.getElementById('movie-list');
    const API_URL = '/api/movies';

    // Función para obtener y mostrar todas las películas
    const fetchMovies = async () => {
        try {
            const response = await fetch(API_URL);
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            const movies = await response.json();
            
            movieList.innerHTML = ''; // Limpiar la lista actual
            movies.forEach(movie => {
                const li = document.createElement('li');
                li.innerHTML = `
                    <div>
                        <span class="movie-info">${movie.title} (${movie.year})</span><br>
                        <span class="movie-details">Dir: ${movie.director} | Rating: ${movie.rating}</span>
                    </div>
                    <span>ID: ${movie.id}</span>
                `;
                movieList.appendChild(li);
            });
        } catch (error) {
            console.error('Error fetching movies:', error);
            movieList.innerHTML = '<li>Error al cargar las películas.</li>';
        }
    };

    // Event listener para el formulario de añadir película
    movieForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const movieData = {
            title: document.getElementById('title').value,
            director: document.getElementById('director').value,
            year: parseInt(document.getElementById('year').value),
            rating: parseFloat(document.getElementById('rating').value)
        };

        try {
            await fetch(API_URL, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(movieData)
            });
            movieForm.reset(); // Limpiar el formulario
            fetchMovies(); // Recargar la lista de películas
        } catch (error) {
            console.error('Error adding movie:', error);
        }
    });

    // Carga inicial de las películas al cargar la página
    fetchMovies();
});