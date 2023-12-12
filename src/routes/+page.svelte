<script lang="ts">
	import EndModal from './EndModal.svelte';
	import type { ComponentEvents } from 'svelte';
	import Card from './Card.svelte';
	import { nextSong } from '$lib/client';
	import type { Song } from './+page.server';
	import { highScore } from '$lib/stores';
	import { timesPlayed } from '$lib/stores';

	export let data;

	// Carousel
	let base = data.base;
	let cur = data.cur;
	let next = data.next;

	// Animation
	let animate = false;
	let rerender = false; // trigger

	// Game logic
	let score = 0;
	let prevScore = score;
	let endScreen = false;

	// Stats
	let inPlay = false;

	async function getColor(song: Song) {
		const imgUrl = song.image.split('/');
		const response = await fetch('/api/color?img=' + imgUrl[imgUrl.length - 1]);
		const color = await response.json();
		song.color = color.color;

		rerender = !rerender;
	}

	function endGame() {
		highScore.update((n) => Math.max(n, score));
		prevScore = score;
		score = 0;
		endScreen = true;
		inPlay = false;
	}

	async function handleGuess(event: ComponentEvents<Card>['guess']) {
		if (!inPlay) {
			inPlay = true;
			timesPlayed.update((n) => n + 1);
		}

		if (event.detail.guess === 'higher') {
			if (cur.streams > base.streams) {
				score++;
			} else {
				endGame();
			}
		} else {
			if (cur.streams < base.streams) {
				score++;
			} else {
				endGame();
			}
		}

		animate = true;
		setTimeout(async () => {
			animate = false;
			base = cur;
			cur = next;
			next = (await nextSong(1))[0];
			await getColor(next);
		}, 1000);
	}
</script>

<div class=" bg-cd-green h-screen w-screen overflow-hidden absolute">
	{#key base.id}
		<section
			class="{animate
				? 'carousel-animation'
				: ''} h-full w-[calc(50%-0.125rem)] absolute left-0 bg-cd-dark"
		>
			<Card {...base} color={base.color} />
		</section>
		<section
			class="{animate
				? 'carousel-animation'
				: ''} h-full w-[calc(50%-0.125rem)] absolute right-0 bg-cd-dark"
		>
			<Card on:guess={handleGuess} {...cur} color={cur.color} guess={true} answer={base.streams} />
		</section>
	{/key}
	{#key rerender}
		<section
			class="{animate
				? 'carousel-animation'
				: ''} h-full w-[calc(50%-0.125rem)] absolute left-[calc(100%+0.26rem)] bg-cd-dark"
		>
			<Card on:guess={handleGuess} {...next} color={next.color} guess={true} />
		</section>
	{/key}
</div>

<p class="text-white absolute bottom-0 pl-5 text-3xl pb-5">
	High Score: {$highScore}
</p>
<p class=" text-white absolute bottom-0 right-0 pr-5 text-3xl pb-5">
	Score: {score}
</p>

<EndModal bind:endScreen>
	<h2 slot="header" class="text-5xl font-bold text-center text-cd-green">{prevScore}</h2>
	<p>High Score: {$highScore}</p>
	<p>Nice try</p>
</EndModal>

<style>
	@keyframes moveLeft {
		0% {
			transform: translateX(0);
		}
		100% {
			transform: translateX(calc(-100% - 0.25rem));
		}
	}

	.carousel-animation {
		animation: moveLeft 1s ease-in-out;
	}
</style>
