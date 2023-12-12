/** @type {import('tailwindcss').Config} */
export default {
	content: ['./src/**/*.{html,js,svelte,ts}'],
	theme: {
		extend: {
			colors: {
				'cd-gray': '#282828',
				'cd-dark': '#121212',
				'cd-green': '#1ED760',
				'cd-light': '#777777',
				'cd-red': '#D6241E'
			},
			screens: {
				sm: '696px'
			}
		}
	},
	plugins: []
};
