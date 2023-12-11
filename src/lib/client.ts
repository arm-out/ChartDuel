import { createClient } from '@supabase/supabase-js';
import type { Tables } from '$lib/types/supabase';

export const supabase = createClient(
	'https://bpzytemgdlcsjopsqpjs.supabase.co',
	'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJwenl0ZW1nZGxjc2pvcHNxcGpzIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDIxNzEzNDUsImV4cCI6MjAxNzc0NzM0NX0.QBoRCDyov8LPyWqVvON711ba3Ae3OrReDlnhBQZvxd4'
);

export const nextSong = async (n: number) => {
	const { data } = await supabase.from('random_songs').select('*').limit(n);
	return data as Tables<'songs'>[];
};
