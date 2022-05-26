<svelte:head>
  <title>My Blog</title>
</svelte:head>

<h1>Blog</h1>

 
  {#each $posts as post}
<h2>{post.title}</h2>
<p>{post.body}</p>
{/each}


<script lang="ts">
  import  {posts} from "../stores/posts";
</script>

