import { writable } from "svelte/store";

export type Post = {
	_id: string;
	title: string;
	slug: string;
	categories: string[];
	body: string;
	created_at: string;
};

export const posts = writable(Array<Post>());

const fetchPosts = async () => {
	const url = "http://127.0.0.1:8000/posts/";
	const response = await fetch(url);
	const data = await response.json();
	const loadedPosts: Post[] = data.map((data: Post) => {
		return {
			...data
		};
	});
	posts.set(loadedPosts);
};
fetchPosts();
