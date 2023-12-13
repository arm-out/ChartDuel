<script lang="ts">
	import { browser } from '$app/environment';
	import { page } from '$app/stores';
	import { createEventDispatcher, onDestroy, onMount } from 'svelte';

	export let title: string;
	export let artist: string;
	export let image: string;
	export let streams: number;
	export let color: string;
	export let guess: boolean = false;
	export let answer: number = 0;
	export let release_date: string;

	const dispatch = createEventDispatcher();
	let innerWidth = browser ? window.innerWidth : 1920;

	let hasGuessed = false;
	let countDisplay = 0;
	let speed = 200;
	let textColor = 'text-white';
	let guessBtn: string = '';

	let year = release_date.split('-')[0];
	$: year = release_date.split('-')[0];

	function animate() {
		const time = streams / speed;
		if (countDisplay < streams) {
			countDisplay = Math.ceil(countDisplay + time);
			setTimeout(animate, 1);
		} else {
			countDisplay = streams;
			setTimeout(() => {
				if (
					(guessBtn === 'higher' && streams > answer) ||
					(guessBtn === 'lower' && streams < answer)
				) {
					textColor = 'text-cd-green';
				} else {
					textColor = 'text-cd-red';
				}
			}, 250);
		}
	}

	function handleGuess(g: 'higher' | 'lower') {
		hasGuessed = true;
		console.log('guessing', g);
		guessBtn = g;
		animate();

		setTimeout(() => {
			dispatch('guess', { guess: g });
		}, 1750);
	}
</script>

<svelte:window bind:innerWidth />

{#if innerWidth > 696}
	<div
		class="card-container h-screen flex flex-col flex-initial items-center pt-[20vh] space-y-12 transition-all duration-500"
		style="background-image: linear-gradient({color}, #121212)"
	>
		<div>
			<img src={image} class="h-80" alt={title} />
			<p class="text-white w-80 pt-5 text-3xl">{title}</p>
			<p class="text-cd-light w-80 pt-2 text-xl">{artist}</p>
		</div>

		<div class="flex flex-col items-center">
			{#if !guess}
				<p class="text-cd-green text-6xl font-bold">{streams?.toLocaleString()}</p>
				<p class="text-cd-light pt-1">
					Total {$page.params.chart == 'global' ? 'global' : 'US'} streams
				</p>
			{:else if !hasGuessed}
				<button
					on:click={() => handleGuess('higher')}
					class="text-white text-xl p-4 px-12 bg-cd-dark border-2 border-solid border-cd-green rounded-full mb-3"
					>Higher</button
				>
				<button
					on:click={() => handleGuess('lower')}
					class="text-white text-xl p-4 px-12 bg-cd-dark border-2 border-solid border-cd-red rounded-full"
					>Lower</button
				>

				{#if year <= 2014}
					<p class="text-gray-300 mt-5">Streams in the Top 100 from 2014 onwards</p>
				{/if}
			{:else}
				<p class="{textColor} text-6xl font-bold transition-colors duration-200">
					{countDisplay.toLocaleString()}
				</p>
				<p class="text-cd-light pt-1">
					Total {$page.params.chart == 'global' ? 'global' : 'US'} streams
				</p>
			{/if}
		</div>
	</div>

	<!-- MOBILE VIEW -->
{:else}
	<div class="h-full w-full bg-cover" style="background-image: url({image})">
		<div class="h-full w-full bg-black/80 flex flex-col items-center justify-center">
			<h2 class="text-white w-[50%] text-center text-2xl">{title}</h2>
			<p class="text-cd-light">{artist}</p>
			{#if !guess}
				<p class="text-cd-green text-5xl font-bold mt-5">{streams?.toLocaleString()}</p>
				<p class="text-cd-light pt-1">
					Total {$page.params.chart == 'global' ? 'global' : 'US'} streams
				</p>
			{:else if !hasGuessed}
				<button
					on:click={() => handleGuess('higher')}
					class="text-white text-lg p-2 px-12 border-2 border-solid border-cd-green rounded-full mb-2 mt-5"
					>Higher</button
				>
				<button
					on:click={() => handleGuess('lower')}
					class="text-white text-lg p-2 px-12 border-2 border-solid border-cd-red rounded-full"
					>Lower</button
				>

				{#if year <= 2014}
					<p class="text-gray-300 mt-5">Streams in the Top 100 from 2014 onwards</p>
				{/if}
			{:else}
				<p class="{textColor} text-5xl font-bold transition-colors duration-200 mt-5">
					{countDisplay.toLocaleString()}
				</p>
				<p class="text-cd-light pt-1">
					Total {$page.params.chart == 'global' ? 'global' : 'US'} streams
				</p>
			{/if}
		</div>
	</div>
{/if}
