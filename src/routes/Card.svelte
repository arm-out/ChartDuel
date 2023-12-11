<script lang="ts">
	import { createEventDispatcher } from 'svelte';

	export let title: string | null;
	export let artist: string | null;
	export let image: string | null;
	export let streams: number;
	export let color: string | undefined;
	export let guess: boolean = false;

	const dispatch = createEventDispatcher();

	let hasGuessed = false;

	function handleGuess(g: 'higher' | 'lower') {
		hasGuessed = true;
		dispatch('guess', { guess: g });
		hasGuessed = false;
	}
</script>

<div
	class="card-container h-screen flex flex-col flex-initial items-center pt-[20vh] space-y-12"
	style="background-image: linear-gradient({color}, #121212)"
>
	<div>
		<img src={image} class="h-80" alt={title} />
		<p class="text-white w-80 pt-5 text-3xl">{title}</p>
		<p class="text-spotify-light w-80 pt-2 text-xl">{artist}</p>
	</div>

	<div class="flex flex-col items-center">
		{#if !guess}
			<p class="text-spotify-green text-6xl font-bold">{streams?.toLocaleString()}</p>
			<p class="text-spotify-light pt-1">Total global streams</p>
		{:else if !hasGuessed}
			<button
				on:click={() => handleGuess('higher')}
				class="text-white text-xl p-4 px-12 bg-spotify-dark border-2 border-solid border-spotify-green rounded-full mb-3"
				>Higher</button
			>
			<button
				on:click={() => handleGuess('lower')}
				class="text-white text-xl p-4 px-12 bg-spotify-dark border-2 border-solid border-red-700 rounded-full"
				>Lower</button
			>
		{:else}
			<p class="text-white text-6xl font-bold">{streams.toLocaleString()}</p>
			<p class="text-spotify-light pt-1">Total global streams</p>
		{/if}
	</div>
</div>
