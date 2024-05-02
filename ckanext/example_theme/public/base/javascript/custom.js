function toggleListVisibility(listId) {
    var listElement = document.getElementById(listId);
    if (listElement) {
        if (listElement.classList.contains('hidden')) {
            listElement.classList.remove('hidden');
        } else {
            listElement.classList.add('hidden');
        }
    }
}