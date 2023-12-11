<script lang="ts">
	import type { ComponentEvents } from 'svelte';
	import Card from './Card.svelte';
	import { nextSong } from '$lib/client';
	import type { Song } from './+page.server';
	export let data;

	let base = data.base;
	let cur = data.cur;
	let next = data.next;

	$: preloadUrl = next.image;

	// Game logic
	let score = 0;
	let highScore = 0;

	async function getColor(song: Song) {
		const imgUrl = song.image.split('/');
		const response = await fetch('/api/color?img=' + imgUrl[imgUrl.length - 1]);
		const color = await response.json();
		song.color = color.color;
	}

	async function handleGuess(event: ComponentEvents<Card>['guess']) {
		if (event.detail.guess === 'higher') {
			if (cur.streams > base.streams) {
				score++;
			} else {
				highScore = Math.max(score, highScore);
				score = 0;
			}
		} else {
			if (cur.streams < base.streams) {
				score++;
			} else {
				highScore = Math.max(score, highScore);
				score = 0;
			}
		}

		base = cur;
		cur = next;
		next = (await nextSong(1))[0];
		await getColor(next);
	}
</script>

<svelte:head>
	<link rel="preload" as="image" href={preloadUrl} />
</svelte:head>

<div class="grid grid-cols-2 gap-1 bg-spotify-green">
	<Card {...base} color={base.color} />
	<Card on:guess={handleGuess} {...cur} color={cur.color} guess={true} />
</div>

<p class=" text-white absolute bottom-0 pl-5 text-3xl pb-5">
	High Score: {highScore}
</p>
<p class=" text-white absolute bottom-0 right-0 pr-5 text-3xl pb-5">
	Score: {score}
</p>
