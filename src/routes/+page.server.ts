import { nextSong } from '$lib/client';

export interface Song {
	artist: string;
	id: string;
	image: string;
	streams: number;
	title: string;
	color?: string;
}

export async function load(event) {
	const data: Song[] = await nextSong(3);
	for (const song of data) {
		const imgUrl = song.image.split('/');
		const response = await event.fetch('/api/color?img=' + imgUrl[imgUrl.length - 1]);
		const color = await response.json();
		song.color = color.color;
	}

	return {
		base: data[0],
		cur: data[1],
		next: data[2]
	};
}
