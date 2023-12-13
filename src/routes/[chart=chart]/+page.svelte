<script lang="ts">
	import { browser } from '$app/environment';
	import EndModal from './EndModal.svelte';
	import { onDestroy, type ComponentEvents, onMount } from 'svelte';
	import Card from './Card.svelte';
	import { nextSong } from '$lib/client';
	import type { Song } from './+page.server';
	import { highScore, playPreviews } from '$lib/stores';
	import { timesPlayed } from '$lib/stores';
	import Github from '~icons/devicon/github';
	import { page } from '$app/stores';
	import { get } from 'svelte/store';

	export let data;

	// Carousel
	let base = data.base;
	let cur = data.cur;
	let buffer = data.buffer;

	let chart = $page.params.chart;
	let genres = $page.url.searchParams.get('genres')?.split(' ') ?? [];

	// Dynamic sizing
	let innerWidth = browser ? window.innerWidth : 1920;

	// Animation
	let animate = false;
	let rerender = false; // trigger

	// Game logic
	let score = 0;
	let prevScore = score;
	let endScreen = false;

	// Stats
	let inPlay = false;

	let audio: HTMLAudioElement;

	onMount(() => {
		if (browser) {
			audio = document.createElement('audio');
			audio.src = cur.preview!;
			audio.play().catch((e) => playPreviews.set(false));
		}

		playPreviews.subscribe((n) => {
			if (n) {
				audio.play().catch((e) => playPreviews.set(false));
			} else {
				audio.pause();
			}
		});
	});

	$: if (browser && audio) {
		audio.src = cur.preview!;
		audio.load();
		if (get(playPreviews) && !endScreen) {
			audio.play().catch((e) => playPreviews.set(false));
		}
	}

	function handleMute() {
		playPreviews.update((n) => !n);
	}

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
			cur = buffer.shift() as Song;
			const next = (await nextSong(1, chart, genres))[0] as Song;
			await getColor(next);
			buffer.push(next);
		}, 1000);
	}
</script>

<svelte:window bind:innerWidth />

<!-- Preload preview songs -->
<svelte:head>
	{#each buffer as song}
		<link rel="prefetch" href={song.preview} as="" />
	{/each}
</svelte:head>

{#if browser}
	{#if innerWidth > 696}
		<div class=" bg-cd-green h-screen w-screen overflow-hidden absolute">
			<a href="/"
				><img src="Logo.svg" alt="ChartDuel" class="absolute z-10 h-[5rem] top-5 left-5" /></a
			>
			<div class="absolute z-10 top-10 right-8">
				<p class="text-xl text-gray-300">
					Built by <a class="hover:text-white font-bold" href="https://github.com/arm-out/ChartDuel"
						><span class="underline">arm-out</span>&nbsp
						<Github class="text-xl" style="fill: white; font-size: 1.2rem; display: inline" />
					</a>
				</p>
			</div>

			{#key base.title}
				<section
					class="{animate
						? 'carousel-left'
						: ''} h-full w-[calc(50%-0.125rem)] absolute left-0 bg-cd-dark"
				>
					<Card {...base} />
				</section>
				<section
					class="{animate
						? 'carousel-left'
						: ''} h-full w-[calc(50%-0.125rem)] absolute right-0 bg-cd-dark"
				>
					<Card on:guess={handleGuess} {...cur} guess={true} answer={base.streams} />
				</section>
			{/key}
			{#key rerender}
				<section
					class="{animate
						? 'carousel-left'
						: ''} h-full w-[calc(50%-0.125rem)] absolute left-[calc(100%+0.26rem)] bg-cd-dark"
				>
					<Card on:guess={handleGuess} {...buffer[0]} guess={true} />
				</section>
			{/key}
		</div>

		<p class="text-white absolute bottom-0 pl-5 text-3xl pb-5">
			High Score: {$highScore}
		</p>
		<p class=" text-white absolute bottom-0 right-0 pr-5 text-3xl pb-5">
			Score: {score}
		</p>

		<!-- svelte-ignore a11y-no-static-element-interactions -->
		<svg
			xmlns="http://www.w3.org/2000/svg"
			class="h-10 w-10 mt-5 cursor-pointer absolute bottom-3 left-[calc(50%+1.5rem)] z-10"
			on:click={handleMute}
			viewBox="0 0 21 21"
			{...$$props}
		>
			{#if $playPreviews}
				<path
					fill="none"
					stroke="#888888"
					stroke-linecap="round"
					stroke-linejoin="round"
					d="M4.5 7.5h3l5-5v16l-5-5h-3a1 1 0 0 1-1-1v-4a1 1 0 0 1 1-1m10 8c1.333-1 2-2.667 2-5s-.667-4-2-5m0 3v4"
				/>
			{:else}
				<path
					fill="none"
					stroke="#888888"
					stroke-linecap="round"
					stroke-linejoin="round"
					d="M11.5 9.5v9l-5-5h-3a1 1 0 0 1-1-1v-4a1 1 0 0 1 1-1h3L8 6m1.521-1.521L11.5 2.5v5m-6-4l12 12m-4-7v1m2.22 4.208c-.337.475-1.077 1.073-2.22 1.792m0-4v1m3-.5v-1.5c0-1.828-.833-3.328-2.5-4.5"
				/>
			{/if}
		</svg>

		<!-- MOBILE VIEW -->
	{:else}
		<div class=" bg-cd-green h-[100dvh] w-screen overflow-hidden absolute">
			{#key base.title}
				<section
					class="{animate
						? 'carousel-up'
						: ''} h-[calc(50%-0.125rem)] w-full absolute top-0 bg-cd-dark"
				>
					<Card {...base} color={base.color} />
				</section>
				<section
					class="{animate
						? 'carousel-up'
						: ''} h-[calc(50%-0.125rem)] w-full absolute bottom-0 bg-cd-dark"
				>
					<Card
						on:guess={handleGuess}
						{...cur}
						color={cur.color}
						guess={true}
						answer={base.streams}
					/>
				</section>
			{/key}
			{#key rerender}
				<section
					class="{animate
						? 'carousel-up'
						: ''} h-[calc(50%-0.125rem)] w-full absolute top-[calc(100%+0.26rem)] bg-cd-dark"
				>
					<Card on:guess={handleGuess} {...buffer[0]} guess={true} />
				</section>
			{/key}

			<p class="text-white absolute top-5 left-5 text-m">
				High Score: {$highScore}
			</p>
			<p class=" text-white absolute top-5 right-5 text-m">
				Score: {score}
			</p>

			<!-- svelte-ignore a11y-no-static-element-interactions -->
			<svg
				xmlns="http://www.w3.org/2000/svg"
				class="h-10 w-10 mt-5 cursor-pointer absolute bottom-3 left-5 z-10"
				on:click={handleMute}
				viewBox="0 0 21 21"
				{...$$props}
			>
				{#if $playPreviews}
					<path
						fill="none"
						stroke="#888888"
						stroke-linecap="round"
						stroke-linejoin="round"
						d="M4.5 7.5h3l5-5v16l-5-5h-3a1 1 0 0 1-1-1v-4a1 1 0 0 1 1-1m10 8c1.333-1 2-2.667 2-5s-.667-4-2-5m0 3v4"
					/>
				{:else}
					<path
						fill="none"
						stroke="#888888"
						stroke-linecap="round"
						stroke-linejoin="round"
						d="M11.5 9.5v9l-5-5h-3a1 1 0 0 1-1-1v-4a1 1 0 0 1 1-1h3L8 6m1.521-1.521L11.5 2.5v5m-6-4l12 12m-4-7v1m2.22 4.208c-.337.475-1.077 1.073-2.22 1.792m0-4v1m3-.5v-1.5c0-1.828-.833-3.328-2.5-4.5"
					/>
				{/if}
			</svg>
		</div>
	{/if}

	<!-- SERVER PRERENDER -->
{:else}
	<div class="h-screen w-screen bg-cd-dark flex items-center justify-center"></div>
{/if}

<EndModal bind:endScreen>
	<h2 slot="header" class="text-5xl font-bold text-center text-cd-green">{prevScore}</h2>
	<!-- <p>Surely we can do better than that right?</p> -->
	<div class="grid grid-cols-2 mb-10">
		<div class="flex flex-col items-center">
			<p class="text-4xl font-bold text-gray-300">{$highScore}</p>
			<p class="text-cd-light">High score</p>
		</div>
		<div class="flex flex-col items-center">
			<p class="text-4xl font-bold text-gray-300">{$timesPlayed}</p>
			<p class="text-cd-light">Plays</p>
		</div>
	</div>
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

	.carousel-left {
		animation: moveLeft 1s ease-in-out;
	}

	@keyframes moveup {
		0% {
			transform: translateY(0);
		}
		100% {
			transform: translateY(calc(-100% - 0.25rem));
		}
	}

	.carousel-up {
		animation: moveup 1s ease-in-out;
	}
</style>
