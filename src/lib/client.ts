import { createClient } from '@supabase/supabase-js';

export const supabase = createClient(
	'https://bpzytemgdlcsjopsqpjs.supabase.co',
	'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJwenl0ZW1nZGxjc2pvcHNxcGpzIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDIxNzEzNDUsImV4cCI6MjAxNzc0NzM0NX0.QBoRCDyov8LPyWqVvON711ba3Ae3OrReDlnhBQZvxd4'
);

export type Query = {
	title: string;
	artist: string;
	streams: number;
	image: string;
	preview?: string;
	url: string;
	release_date: string;
};

export const nextSong = async (n: number, chart: string, genres: string[]) => {
	const filter = genres.map((genre) => `${genre}.eq.true`).join(',');

	if (genres.length === 0) {
		const { data } = await supabase
			.from(`${chart}_random`)
			.select('title, artist, streams, image, preview, url, release_date')
			.limit(n);
		return data as Query[];
	}

	const { data } = await supabase
		.from(`${chart}_random`)
		.select('title, artist, streams, image, preview, url, release_date')
		.or(filter)
		.limit(n);
	return data as Query[];
};

export const getCount = async (chart: string, genres: string[]) => {
	const filter = genres.map((genre) => `${genre}.eq.true`).join(',');

	if (genres.length === 0) {
		const { count } = await supabase.from(`${chart}_random`).select('*', { count: 'exact' });
		return count;
	}

	const { count } = await supabase
		.from(`${chart}_random`)
		.select('*', { count: 'exact' })
		.or(filter);
	return count;
};
