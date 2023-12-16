<script>
	import '../app.css';
	import { injectSpeedInsights } from '@vercel/speed-insights/sveltekit';
	import { dev } from '$app/environment';
	import { inject } from '@vercel/analytics';

	inject({ mode: dev ? 'development' : 'production' });

	injectSpeedInsights();
</script>

<svelte:head>
	<meta name="description" content="Play a game of higher or lower with the Spotify charts!" />
	<meta property="og:title" content="ChartDuels" />
	<meta
		property="og:description"
		content="Play a game of higher or lower with the Spotify charts!"
	/>
	<meta property="og:image" content="/og-image.png" />
	<meta property="og:url" content="https://chartduels.com" />
	<meta property="og:type" content="website" />

	<title>ChartDuels</title>
</svelte:head>

<slot />
