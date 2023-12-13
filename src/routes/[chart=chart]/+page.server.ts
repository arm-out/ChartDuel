import { nextSong, type Query } from '$lib/client';

export type Song = Query & { color: string };

export async function load({ fetch, params, url }) {
	const data: Song[] = (await nextSong(
		4,
		params.chart,
		url.searchParams.get('genres')?.split(' ') ?? []
	)) as Song[];

	await Promise.all(
		data.map(async (song) => {
			const imgUrl = song.image.split('/');
			const response = await fetch('/api/color?img=' + imgUrl[imgUrl.length - 1]);
			const color = await response.json();
			song.color = color.color;
		})
	);

	return {
		base: data[0],
		cur: data[1],
		buffer: [data[2], data[3]],
		chart: params.chart
	};
}
