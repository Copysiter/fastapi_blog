<svelte:head>
	<title>My Blog</title>
</svelte:head>

<h1>Blog</h1>

<button>Add Post ✒️</button>
<input type="text" placeholder="🔍 Search post..." bind:value={searchTerm}/>

<div class="posts">
	{#each filteredPosts as post}
	<PostComponent {post} />
{/each}
</div>

<script context="module" lang="ts">
  // @ts-ignore
  export const load = async ({params, fetch}) => {
    const url = "http://127.0.0.1:8000/posts/";
		const response = await fetch(url);
		const data = await response.json();
		const loadedPosts: Post[] = data.map((data: Post) => {
		return {
			...data
		};
	});
	return {props : {posts : loadedPosts}}
  }
</script>

<script lang="ts">
	import type { Post } from "../stores/posts"
	export let posts : Post[];
	let searchTerm = ""
	let filteredPosts = Array<Post>()

	$: {
		if (searchTerm) {
			filteredPosts = posts.filter(post => {
				return post.title.toLowerCase().includes(searchTerm.toLocaleLowerCase())
			})
		} else {
			filteredPosts = [...posts]
		}
	}
	import PostComponent from "../components/post.svelte";
</script>
