<script lang="ts">
	let props = {
		class: [$$restProps.class]
	};
</script>

<button
	on:click
	on:mouseover
	on:focus
	on:mouseenter
	on:mouseleave
	{...props}
	class="text-xl p-4 px-12 rounded-full outline-none"><slot /></button
>
