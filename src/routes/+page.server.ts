import { getCount } from '$lib/client.js';

export async function load() {
	const us_count = await getCount('us', []);
	const global_count = await getCount('global', []);

	return {
		us_count,
		global_count
	};
}
