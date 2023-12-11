import { json, type RequestHandler } from '@sveltejs/kit';
import Vibrant from 'node-vibrant';

export const GET: RequestHandler = async ({ url }) => {
	const imgUrl = 'https://i.scdn.co/image/' + url.searchParams.get('img');
	const palette = await Vibrant.from(imgUrl).getPalette();
	let color;
	if (palette.DarkVibrant) {
		color = palette.DarkVibrant.rgb.map((c: number) => Math.round(c));
	} else {
		color = [18, 18, 18];
	}
	return json({ color: rgbToHex(color) });
};

const rgbToHex = (rgb: number[]) =>
	'#' + rgb.map((c: number) => c.toString(16).padStart(2, '0')).join('');
