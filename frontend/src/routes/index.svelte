<svelte:head>
	<title>My Blog</title>
</svelte:head>

<h1>Blog</h1>

{#each $posts as post}
	<PostComponent {post} />
{/each}

<script lang="ts">
	import { posts } from "../stores/posts";
	import PostComponent from "../components/post.svelte";
</script>