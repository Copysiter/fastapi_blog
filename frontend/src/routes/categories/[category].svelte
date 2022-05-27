<svelte:head>
  <title>{category}</title>
</svelte:head>

<h1>{category}</h1>
{#each posts as post}
<a href={`/posts/${post.slug}`}>
		<h2>{post.title}</h2>
</a>
{post.created_at}
<a href={`/categories/${category}`}><span>{category}</span></a>
<p>{`${post.body.slice(0,400)}...`}</p>
{/each}

<script context="module">
  // @ts-ignore
  export const load = async ({params, fetch}) => {
    const category = params.category;
    const url = `http://127.0.0.1:8000/categories/${category}`;
    const response = await fetch(url);
    const posts = await response.json();
    return {props : {posts : posts, category : category}};
  }
</script>
<script lang="ts">
  import type { Post} from "../../stores/posts"
  export let  posts : Post[];
  export let category : string;
</script>