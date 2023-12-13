import { browser } from '$app/environment';
import { writable } from 'svelte/store';

export const highScore = writable(
	browser && localStorage.getItem('highScore') ? parseInt(localStorage.getItem('highScore')!) : 0
);
highScore.subscribe((value) => browser && localStorage.setItem('highScore', String(value)));

export const timesPlayed = writable(
	browser && localStorage.getItem('timesPlayed')
		? parseInt(localStorage.getItem('timesPlayed')!)
		: 0
);
timesPlayed.subscribe((value) => browser && localStorage.setItem('timesPlayed', String(value)));

export const playPreviews = writable(true);
