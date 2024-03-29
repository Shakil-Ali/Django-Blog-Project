// Variables (constants) for fields we want to fill in and populate
const titleInput = document.querySelector('input[name=title]');
const slugInput = document.querySelector('input[name=slug]');

const slugify = (val) => {
	return val.toString().toLowerCase().trim()
		.replace(/&/g, '-and-') // replace & with '-and-' for slugs
		.replace(/[\s\W-]+/g, '-') // replaces spaces, non-word chars and dashes with a single dash
};

titleInput.addEventListener('keyup', (e) => {
	slugInput.setAttribute('value', slugify(titleInput.value));
});

