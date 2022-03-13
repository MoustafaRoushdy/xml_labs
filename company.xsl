<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
<html>
    <h2>Company</h2>
    <table border = "1">
        <tr>
            <th>Name</th>
            <th>Phone</th>
            <th>Address</th>
            <th>Email</th>
        </tr>
        <xsl:for-each select="company/employee">
        <tr>
            <td><xsl:value-of select="name"/></td>
            <td><xsl:value-of select="phones/phone[@type = 'mobile'"/></td>
            <td><xsl:value-of select="addresses/address[1]"/></td>
            <td><xsl:value-of select="email"/></td>

        </tr>
        </xsl:for-each>
    </table>
</html>
</xsl:template>
</xsl:stylesheet>