<script lang="ts">
	import RadioBtn from './RadioBtn.svelte';
	import { goto } from '$app/navigation';
	import { getCount } from '$lib/client';
	import type { ComponentEvents } from 'svelte';

	export let data;

	let us_count = data.us_count;
	let global_count = data.global_count;

	let genres: string[] = [];
	let params = '?genres';

	$: if (genres.length > 0) {
		params = '?genres=' + genres.join('+');
	} else {
		params = '';
	}

	async function genreChange(event: ComponentEvents<RadioBtn>['genres']) {
		genres = event.detail.genres;
		us_count = await getCount('us', genres);
		global_count = await getCount('global', genres);
	}
</script>

<div class="flex flex-col h-screen w-screen items-center justify-top bg-cd-dark overflow-hidden">
	<h1 class="invisible">ChartDuels!</h1>
	<img src="Logo.svg" alt="ChartDuels" class=" max-w-2xl w-[80%]" />
	<h2 class="text-xl sm:text-2xl w-[80%] mt-5 mb-[10dvh] text-center text-white">
		Play a game of higher or lower with the Spotify charts!
	</h2>

	<div class="flex flex-col w-screen items-center gap-5">
		<button
			class="bg-cd-green w-[80%] max-w-sm rounded-full text flex flex-col items-center justify-center font-bold text-2xl pt-5 py-4"
			on:click={() => goto(`us${params}`)}
			>Play US Charts<span class="font-normal text-base">{us_count} songs</span></button
		>
		<button
			class="bg-cd-green w-[80%] max-w-sm rounded-full text flex flex-col items-center justify-center font-bold text-2xl pt-5 py-4"
			on:click={() => goto(`global${params}`)}
			>Play Global Charts<span class="font-normal text-base">{global_count} songs</span></button
		>
	</div>

	<div>
		<h3 class="text-cd-light text-2xl mt-20 mb-[5%] text-center">Genres</h3>
		<RadioBtn on:genres={genreChange} />
	</div>
</div>
