<script lang="ts">
    import { onMount } from "svelte";
    import { db } from "$lib/sqlite";
	import { goto } from "$app/navigation";

    onMount( async () => {
        type Table = {
            name: string
        }

        const user_data_table: Table = await db.select(`
            SELECT name 
            FROM sqlite_master 
            WHERE type='table' AND name='userData'
        `);

        if (!user_data_table) {
            goto('/auth');
        }
    })
</script>