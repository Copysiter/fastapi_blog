<a href={`/posts/${post.slug}`}><h2>{post.title}</h2></a>
{post.created_at} || 
{#each post.categories as category}
<span>{category}</span>
{/each}
<p>{post.body}</p>

<script lang="ts">
	import type { Post } from "../stores/posts";
	export let post: Post;
</script>