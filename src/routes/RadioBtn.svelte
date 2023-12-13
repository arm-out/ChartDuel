<script lang="ts">
	import { createEventDispatcher } from 'svelte';

	let genres: string[] = [];

	let unchecked = 'text-white font-light';
	let checked = 'text-black bg-gray-400 font-base';

	let all_checked = 'border-cd-green bg-cd-green font-bold';
	let all_unchecked = 'text-white border-white bg-transparent';

	const dispatch = createEventDispatcher();

	$: dispatch('genres', { genres });

	function handleClick(genre: string) {
		if (genres.includes(genre)) {
			genres = genres.filter((g) => g !== genre);
		} else {
			genres.push(genre);
		}

		genres = genres;
	}

	function clickAll() {
		genres = [];
	}
</script>

<div class="w-full flex flex-row flex-wrap gap-x-2 gap-y-2 px-5">
	<button
		on:click={clickAll}
		class="{genres.length == 0
			? all_checked
			: all_unchecked} border rounded-full px-2 text-lg font-bold"
	>
		All
	</button>
	<button
		on:click={() => handleClick('rap')}
		class="{genres.includes('rap')
			? checked
			: unchecked} border rounded-full px-2 border-gray-400 text-lg">Hip-Hop/R&b</button
	>
	<button
		on:click={() => handleClick('pop')}
		class="{genres.includes('pop')
			? checked
			: unchecked} border rounded-full px-2 border-gray-400 text-lg">Pop</button
	>
	<button
		on:click={() => handleClick('latin')}
		class="{genres.includes('latin')
			? checked
			: unchecked} border rounded-full px-2 border-gray-400 text-lg">Latin</button
	>
	<button
		on:click={() => handleClick('kpop')}
		class="{genres.includes('kpop')
			? checked
			: unchecked} border rounded-full px-2 border-gray-400 text-lg">K-Pop</button
	>
	<button
		on:click={() => handleClick('edm')}
		class="{genres.includes('edm')
			? checked
			: unchecked} border rounded-full px-2 border-gray-400 text-lg">EDM/Dance</button
	>
	<button
		on:click={() => handleClick('rock')}
		class="{genres.includes('rock')
			? checked
			: unchecked} border rounded-full px-2 border-gray-400 text-lg">Rock</button
	>
	<button
		on:click={() => handleClick('country')}
		class="{genres.includes('country')
			? checked
			: unchecked} border rounded-full px-2 border-gray-400">Country</button
	>
</div>
