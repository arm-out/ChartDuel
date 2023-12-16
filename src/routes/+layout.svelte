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

	<meta name="twitter:card" content="summary_large_image" />
	<meta name="twitter:title" content="ChartDuels" />
	<meta
		name="twitter:description"
		content="Play a game of higher or lower with the Spotify charts!"
	/>
	<meta name="twitter:image" content="/og-image.png" />
	<meta name="twitter:url" content="https://chartduels.com" />
	<meta name="twitter:creator" content="@armzout" />

	<title>ChartDuels</title>
</svelte:head>

<slot />
