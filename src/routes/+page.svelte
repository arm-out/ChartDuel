<script lang="ts">
	import Card from './Card.svelte';
	export let data;

	let base = data.base;
	let cur = data.cur;
	let next = data.next;
</script>

<div class="grid grid-cols-2 gap-1 bg-spotify-green">
	<Card {...base} />
	<Card {...cur} hidden={true} />
</div>
