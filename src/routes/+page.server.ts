import { nextSong } from '$lib/client';

export async function load() {
	const data = await nextSong(3);
	return {
		base: data[0],
		cur: data[1],
		next: data[2]
	};
}
