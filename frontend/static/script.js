document.addEventListener('DOMContentLoaded', () => {
    const saveButton = document.getElementById('saveButton');
    const input = document.getElementById('catalogueInput');
    const startInput = document.getElementById('startDateInput');
    const endInput = document.getElementById('endDateInput');
    const list = document.getElementById('catalogueList');
    const alertBox = document.getElementById('alertBox');

    function showAlert(message, type = 'success') {
        alertBox.textContent = message;
        alertBox.className = `p-2 rounded mb-4 text-white ${type === 'success' ? 'bg-green-500' : 'bg-red-500'}`;
        alertBox.classList.remove('hidden');
        setTimeout(() => {
            alertBox.classList.add('hidden');
        }, 2500);
    }

    async function loadCatalogues() {
        try {
            const res = await fetch('/catalogues');
            const data = await res.json();
            console.log("Fetched catalogues:", data);

            list.innerHTML = '';
            data.forEach(item => {
                const li = document.createElement('li');
                li.className = 'p-2 bg-gray-100 flex justify-between items-center mb-2';
                li.innerHTML = `
                    <span>
                        <strong>${item.catalogue_name}</strong><br>
                        Start: ${item.start_date}<br>
                        End: ${item.end_date}
                    </span>
                    <button class="bg-red-500 text-white px-2 py-1 rounded delete-btn" data-id="${item.catalogue_id}">Delete</button>
                `;
                list.appendChild(li);
            });

            attachDeleteEvents();
        } catch (err) {
            console.error(err);
            showAlert('Failed to load catalogues.', 'error');
        }
    }

    function attachDeleteEvents() {
        const deleteButtons = document.querySelectorAll('.delete-btn');
        deleteButtons.forEach(button => {
            button.addEventListener('click', async () => {
                const id = button.getAttribute('data-id');
                await deleteCatalogue(id);
            });
        });
    }

    async function deleteCatalogue(id) {
        try {
            const resp = await fetch('/deleteCatalogue', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ id: parseInt(id) })
            });

            const data = await resp.json();
            if (resp.ok && data.status === 'success') {
                showAlert('Catalogue deleted successfully!', 'success');
                loadCatalogues();
            } else {
                showAlert(`Error: ${data.message}`, 'error');
            }
        } catch (err) {
            console.error(err);
            showAlert('Server error while deleting.', 'error');
        }
    }

    saveButton.addEventListener('click', async () => {
        const name = input.value.trim();
        const start_date = startInput.value;
        const end_date = endInput.value;

        if (!name || !start_date || !end_date) {
            showAlert('All fields are required!', 'error');
            return;
        }

        try {
            const res = await fetch('/catalogues', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ name, start_date, end_date })
            });

            const data = await res.json();
            if (res.ok && data.status === 'success') {
                showAlert('Catalogue added successfully!', 'success');
                input.value = '';
                startInput.value = '';
                endInput.value = '';
                loadCatalogues();
            } else {
                showAlert(`Error: ${data.message}`, 'error');
            }
        } catch (err) {
            console.error(err);
            showAlert('Server error while saving!', 'error');
        }
    });

    // Initial call to load existing catalogues
    loadCatalogues();
});
