<script lang="ts">
	export let title: string | null;
	export let artist: string | null;
	export let image: string | null;
	export let streams: number | null;
	export let hidden: boolean = false;
</script>

<div class="bg-spotify-dark h-screen flex flex-col items-center pt-44">
	<img src={image} class="h-80" alt={title} />
	<p class="text-white w-80 pt-5 text-3xl">{title}</p>
	<p class="text-spotify-light w-80 pt-2 text-xl pb-10">{artist}</p>
	{#if !hidden}
		<p class="text-spotify-green text-6xl font-bold">{streams?.toLocaleString()}</p>
		<p class="text-spotify-light pt-1">Total global streams</p>
	{/if}
	{#if hidden}
		<button
			class="text-white text-xl p-4 px-12 bg-spotify-dark border-2 border-solid border-spotify-green rounded-full mb-4"
			>Higher</button
		>
		<button
			class="text-white text-xl p-4 px-12 bg-spotify-dark border-2 border-solid border-red-700 rounded-full bg-"
			>Lower</button
		>
	{/if}
</div>
