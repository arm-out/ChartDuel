<script lang="ts">
	import Button from '$lib/components/Button.svelte';
	import Twitter from '~icons/devicon/twitter';

	export let endScreen = false;
	let dialog: HTMLDialogElement;

	$: if (dialog && endScreen) dialog.showModal();
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<!-- svelte-ignore a11y-no-noninteractive-element-interactions -->
<dialog
	bind:this={dialog}
	on:close={() => (endScreen = false)}
	on:click|self={() => dialog.close()}
	class="h-[100dvh] w-screen sm:min-w-[30rem] sm:w-[30%] sm:min-h-[40%] backdrop:backdrop-blur-sm bg-cd-dark"
>
	<!-- svelte-ignore a11y-no-static-element-interactions -->
	<div on:click|stopPropagation class="py-8 px-5 relative h-full overflow-hidden">
		<img src="Logo.svg" alt="ChartDuel" class="w-[70%] object-center block ml-auto mr-auto mb-4" />

		<slot name="header" />
		<p class="text-cd-light text-center mb-10">Your Score</p>
		<slot />

		<div class="flex gap-2 absolute bottom-5 w-[90%]">
			<!-- svelte-ignore a11y-autofocus -->
			<button
				autofocus
				class="w-full bg-cd-green text-xl px-3 rounded-full outline-none h-[3rem]"
				on:click={() => dialog.close()}>Play Again</button
			>
			<div
				class="bg-black flex items-center justify-center w-full rounded-full h-[3rem] border border-white"
			>
				<a
					href="https://twitter.com/share?ref_src=twsrc%5Etfw"
					target="_blank"
					class="text-white w-full flex items-center justify-center"
					data-size="large"
					data-text="Check out this game of Higher or Lower using @Spotify song streams"
					data-url="https://chartduels.com"
					data-lang="en"
					data-dnt="true"
					data-show-count="false"
					><Twitter style="fill: white; font-size: 1.15rem" />&nbsp &nbsp &nbspShare</a
				>
			</div>
		</div>
	</div>
</dialog>
